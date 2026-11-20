def show_result(result):
    print("\n--- Assessment Result ---")
    print("Suggested interest area:", result["area"])
    print("Score:", result["score"])
    print("\nScores by area:")
    for area, score in result["scores"].items():
        print(f"{area.title()}: {score}")
    print("\nNote: This is a simple educational assessment, not a professional career test.")
