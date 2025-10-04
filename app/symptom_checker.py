import json
import streamlit as st

def load_symptom_data():
    with open("data/symptoms_conditions.json") as f:
        data = json.load(f)
    return data

def check_symptoms(symptoms): 
    data = load_symptom_data()
    result = []                 #? An empty list to collect possible diseases
    
    for symptom in symptoms:
        s = symptom.lower()
        if s in data:
            info = data[s]
            result.append({
                "symptom": s,
                "condition": info["conditions"],
                "severity": info["severity"],
                "causes": info["causes"],
                "first_aid": info["first_aid"]
            })
    return result if result else [{"symptom": "None", "conditions": ["No matches found"], "severity": "-", "causes": [], "first_aid": []}]

def main():
    st.title("Symptom Checker")
    st.write("Select your symptoms below:")
    available_symptoms = ["Fever", "Cough", "Headache"]
    selected = st.multiselect("Symptoms", available_symptoms)
    
    if st.button("check"):
        results = check_symptoms(selected)
        for res in results:
            st.subheader(res["symptom"].capitalize())
            st.write(f"**severity:** {res['severity'].capitalize()}")
            
            st.write("### 🩺 Possible Conditions:")
            for cond in res["condition"]:
                st.write(f"- {cond}")
                
            st.write("### 🧠 Possible Causes:")
            for cause in res["causes"]:
                st.write(f"- {cause}")
                
            st.write("### 🩹 First Aid Suggestions:")
            for tip in res["first_aid"]:
                st.write(f"- {tip}")
                
            st.markdown("---")
            
if __name__ == "__main__":
    main()