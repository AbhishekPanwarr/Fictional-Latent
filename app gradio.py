import gradio as gr
import random

def generate_story(scenario, character1, character2):
    story_templates = [
        f"{character1} and {character2} found themselves in {scenario}. What happened next was beyond imagination...",
        f"In {scenario}, {character1} and {character2} had to make a tough choice. Their journey was about to change forever.",
        f"As {character1} and {character2} explored {scenario}, they encountered a mysterious event that changed everything."
    ]
    
    story = random.choice(story_templates)
    
    # Return the story, plus updates for the visibility of all 5 buttons
    return [story] + [gr.update(visible=True)] * 5  # 1 for story and 5 for buttons

def change_scenario(selected_scenario, character1, character2):
    return generate_story(selected_scenario, character1, character2)[0]

def clear_story():
    return ["The story has ended. Start a new one!"] + [gr.update(visible=False)] * 5  # Hide all buttons

def show_change_buttons():
    return [gr.update(visible=True)] * 3  # Show the change scenario buttons

with gr.Blocks() as demo:
    gr.Markdown("# Interactive Story Generator")
    
    with gr.Row():
        scenario_input = gr.Textbox(label="Starting Scenario")
        character1_input = gr.Textbox(label="Character 1")
        character2_input = gr.Textbox(label="Character 2")
    
    start_btn = gr.Button("Start Story")
    change_scenario_btn = gr.Button("Change Scenario", visible=False)  # Initially hidden
    
    change_scenario_buttons = [
        gr.Button("A new challenge arises", visible=False),
        gr.Button("A twist in the tale", visible=False),
        gr.Button("A surprising ally appears", visible=False)
    ]
    
    end_btn = gr.Button("End Story", visible=False)
    
    story_output = gr.Textbox(label="Story", interactive=False)
    
    # Start button click event
    start_btn.click(generate_story, inputs=[scenario_input, character1_input, character2_input], 
                    outputs=[story_output] + change_scenario_buttons + [end_btn])
    
    # Show the change scenario buttons when "Change Scenario" is clicked
    change_scenario_btn.click(show_change_buttons, outputs=change_scenario_buttons)
    
    # Change scenario buttons click events
    for btn in change_scenario_buttons:
        btn.click(change_scenario, inputs=[scenario_input, character1_input, character2_input], outputs=story_output)
    
    # End button click event
    end_btn.click(clear_story, outputs=[story_output] + change_scenario_buttons + [end_btn])

# Launch the Gradio app
demo.launch()
