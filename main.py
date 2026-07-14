
    import os
import json
from datetime import datetime
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_latest_error():
    """Simulate reading a server error log"""
    return "CRITICAL: nginx service failed to start. Port 80 is already in use by another process."

def analyze_error_with_ai(error_text):
    """Send error to Groq AI and get a diagnosis"""
    print(f"[*] Sending this error to AI: {error_text}")

    prompt = f"""
    You are a senior DevOps engineer. Analyze this server error:
    "{error_text}"
    
    Give me a response in JSON format with these exact keys:
    1. "root_cause": (brief explanation of what's wrong)
    2. "fix_command": (the exact terminal command to fix this)
    3. "risk": (say "High", "Medium", or "Low" risk for running this fix)
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-70b-versatile",  # WORKING model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            response_format={"type": "json_object"}
        )
        
        ai_reply = response.choices[0].message.content
        return json.loads(ai_reply)
        
    except Exception as e:
        print(f"[!] AI Error: {e}")
        return {
            "root_cause": "Unknown (API error - check your key or internet)",
            "fix_command": "sudo systemctl restart nginx",
            "risk": "High"
        }

def save_report(original_error, ai_result):
    """Save the diagnosis to a JSON file"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_data = {
        "timestamp": timestamp,
        "error": original_error,
        "diagnosis": ai_result
    }
    
    if not os.path.exists("reports"):
        os.makedirs("reports")
    
    filename = f"reports/report_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(report_data, f, indent=4)
    
    print(f"[✓] Report saved to {filename}")
    return filename

if __name__ == "__main__":
    print("🤖 AI Auto-Healer Starting...")
    
    error = get_latest_error()
    result = analyze_error_with_ai(error)
    
    print("\n" + "="*50)
    print(f"✅ Root Cause: {result.get('root_cause')}")
    print(f"🛠️  Suggested Fix: {result.get('fix_command')}")
    print(f"⚠️  Risk Level: {result.get('risk')}")
    print("="*50 + "\n")
    
    save_report(error, result)
    print("✨ Done! Check the 'reports' folder.")