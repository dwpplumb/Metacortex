# entrypoint.py

from core.processing import run_pipeline

if __name__ == "__main__":
    input_text = "Was ist der Sinn von Veränderung?"
    result = run_pipeline(input_text)
    print("\n--- Endausgabe ---")
    print(result)
