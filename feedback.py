def count_good_feedback(feedback):
    return feedback.lower().count("good")

def main():
    feedback = input("Enter your feedback: ")
    count = count_good_feedback(feedback)
    print(f"The word 'good' appears {count} times in your feedback.")

if __name__ == "__main__":
    main()
