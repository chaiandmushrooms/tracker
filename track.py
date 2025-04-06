from datetime import date

def formatted_text(text):
    if not text:
        return ("NA")
    else:
        return text.replace(",", " -")


def main():
    #opening file
    data = open("data.csv", 'a')

    time = str(date.today())
    hours = (input("How many hours were spent being productive today: "))
    ticked_items = (input("Enter list of things you got done from your to-do list today: "))
    unticked_items = (input("Enter list of things you didn't get done from your to-do list today: "))
    topics = (input("Enter the topics you focused on today: "))
    composure = (input("How composed are you on those topics (1 - 10): "))
    mood = (input("What is your mood like (1 - 10): "))
    lessons = (input("Your lesson for the day: "))
    blockers = (input("Enter any blockers you might've encountered today: "))
    events = (input("Enter any major event that caused disruption to your plans for the day: "))
    dataset = [time, hours, ticked_items, unticked_items, topics, composure, mood, blockers, events, lessons]

    # writing to file and closing it immediately
    data.write(", ".join(formatted_text(item).strip() for item in dataset) + "\n")
    data.close()
    print ("good job! see you tomorrow \\o/")

if __name__ == "__main__":
    main()