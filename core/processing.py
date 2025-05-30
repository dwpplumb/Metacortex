# core/processing.py

def log_step(step_name, data):
    print(f"\n[{step_name}]")
    print(data)

def superposition_transform(text):
    return {
        "transformed": f"<SP:{text.upper()}>",
        "metadata": {"phase": 1}
    }

def token_processing(transformed_data):
    return f"TOKENS::{transformed_data['transformed']}"

def run_pipeline(text):
    log_step("Input", text)

    sp_result = superposition_transform(text)
    log_step("Superposition", sp_result)

    token_output = token_processing(sp_result)
    log_step("Tokenisierung", token_output)

    return token_output
