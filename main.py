import asyncio
from form_reader import read_form
from agent import fill_with_agent

async def main():
    url = input("Paste form URL: ")
    context = input("Any specific context for this application? (press enter to skip): ")
    
    print("\nReading form...")
    fields = await read_form(url)
    for f in fields:
        print(f)
    
    labelled = [f for f in fields if f['label'] and f['label'] != '{name}' and f['name']]
    print(f"Found {len(labelled)} fields.\n")
    
    print("Generating answers...")
    answers = fill_with_agent(labelled, context if context else None)

    print("\n--- GENERATED ANSWERS ---")
    for field in labelled:
        name = field['name']
        label = field['label']
        answer = answers.get(name, 'N/A')
        if name:  # only print if field has a name
            print(f"\n{label}:\n{answer}")
    
    
    print("\n--- END ---")

asyncio.run(main())
