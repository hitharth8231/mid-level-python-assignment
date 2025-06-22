import os
import csv
import json

def load_scores(path:str):
    records =[]
    if not os.path.exists(path):
        print(" No existing score file found. Starting fresh.")
        return records
    try:
        if path.endswith(".csv"):
            with open(path, mode='r',newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 2:
                        name,score = row[0].strip(),int(row[1])
                        records.append((name,score))
        elif path.endswith(".json"):
            with open(path,mode = 'r') as file:
                records = [(entry["name"],int(entry["scores"])) for entry in json.load(file)]
        else:
            print("Unsupported file format. Starting fresh.")
    except Exception as e:
        print(f"Error reading file: {e}. Starting with an empty list.")
        records=[]
    return records
def save_scores(path: str, records:list[tuple[str,int]]) -> None:
    try:
        if path.endswith(".csv"):
            with open(path , mode='w',newline='') as file:
                writer = csv.writer(file)
                writer.writerows(records)
        elif path.endswith(".json"):
            with open(path, mode ='w') as file:
                json.dump([{"name":name,"score":score} for name, score in records], file, indent=2)
    except Exception as e:
        print(f"Error saving file: {e}")

def add_score(records: list[tuple[str,int]],name: str,score: int) -> None:
    records.append((name,score))

def top_n(records: list[tuple[str,int]],n:int) :
    return sorted(records,key = lambda x:x[1],reverse = True)[:n]

def delete_all_scores(path: str) -> None:
    confirm = input("Type yes if you want to delete all scores")
    if confirm.strip().upper() == "YES":
        try: 
            open(path,'w').close()
            print("All scores deleted")
        except Exception as e:
            print(f"Error deleting scores: {e}")
    else:
        print("Delete cancelled")

def main():
    path = input("Enter the score file name:").strip()
    if not path:
        path = "scores.csv"

    records = load_scores(path)

    while True:
        print("\n Score Menu" \
        "1. Show top N scores" \
        "2.Add New Score" \
        "4.Exit")

        try:
            choice = int(input("Enter your choice:"))
            if choice == 1:
                if not records:
                    print(" No scores")
                    continue
                n = int(input("Enter N: "))
                top_scores = top_n(records,n)
        
            elif choice == 2:
                name = input(" Enter name: ").strip()
                score = int(input("Enter score: "))
                add_score(records,name, score)
                save_scores(path,records)

            elif choice == 3:
                delete_all_scores(path)
                records.clear()

            elif choice == 4:
                print("Exit")
                break
            else:
                print("Enter a valid number")

        except ValueError:
            print("Enter a valid integer")

if __name__ == "__main__":
    main()



            
            
     