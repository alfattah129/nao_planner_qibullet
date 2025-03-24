import openai
import json

# Insert your OpenAI API key directly here
openai.api_key = "Enter your API key here"

class RobotPlanner:
    def __init__(self):
        # Define the available actions based on the Nao class
        self.available_actions = [
            "speak(speech=text)",
            "stand()",
            "sit()",
            "wave(hand=right/left)",
            "nod_head(direction=up_down/right_left)",
            "turn_head(direction=right/left)",
            "gaze_head(direction=up/down)",
            "raise_arms(hand=left/right/both)",
            "move(x=x,y=y,theta=theta)",
            "handshake(hand=right/left)",
            "reset_nao_pose()"
        ]
        self.model = "gpt-3.5-turbo-16k"
        self.max_completion_length = 1000
        
    def generate_plan(self, instruction):
        print(f"Generating plan for instruction: {instruction}")
        
        system_prompt = """You are a robot action planner for a NAO robot. Your task is to create a sequence of actions 
        for the robot to follow based on the instruction. 
        The available actions are:
        - speak(speech=text): Make the robot say the specified text
        - stand(): Make the robot stand up
        - sit(): Make the robot sit down
        - wave(hand=right/left): Make the robot wave with the specified hand
        - nod_head(direction=up_down/right_left): Make the robot nod its head in the specified direction
        - turn_head(direction=right/left): Make the robot turn its head in the specified direction
        - gaze_head(direction=up/down): Make the robot gaze in the specified direction
        - raise_arms(hand=left/right/both): Make the robot raise the specified arm(s)
        - move(x=x,y=y,theta=theta): Make the robot move to the specified position with the specified rotation
        - handshake(hand=right/left): Make the robot perform a handshake with the specified hand
        - reset_nao_pose(): Reset the robot's pose to the default position
        
        Return your action plan in JSON format with the following structure:
        {
            "actions": [
                {
                    "action": "action_name",
                    "parameters": {"param1": "value1", "param2": "value2"}
                }
            ]
        }
        
        Be specific with action parameters and ensure the sequence of actions logically fulfills the instruction.
        """
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Instruction: {instruction}\n\nCreate a detailed action plan for the NAO robot."}
        ]
        
        try:
            print("Sending request to OpenAI API...")
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=0.1,
                max_tokens=self.max_completion_length,
                top_p=0.5,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            
            print("Received response from OpenAI API")
            plan_text = response['choices'][0].message.content
            print(f"Raw response: {plan_text[:100]}...")  # Print first 100 chars
            
            # Extract JSON part if surrounded by backticks
            if '```json' in plan_text:
                plan_text = plan_text.split('```json')[1].split('```')[0].strip()
            elif '```' in plan_text:
                plan_text = plan_text.split('```')[1].split('```')[0].strip()
            
            # Clean up any potential issues with quotes
            plan_text = plan_text.replace("'", "\"")
            
            # Load the plan as JSON
            print("Parsing JSON response...")
            plan = json.loads(plan_text)
            return plan
            
        except Exception as e:
            print(f"Error generating plan: {str(e)}")
            import traceback
            traceback.print_exc()
            return None
    
    def execute_plan(self, plan):
        """
        This function would connect to the NAO robot and execute the planned actions.
        For demonstration, we'll just print the actions.
        """
        if not plan or "actions" not in plan:
            print("Invalid plan received")
            return
        
        print("\n=== Action Plan ===")
        for i, action_item in enumerate(plan["actions"]):
            action = action_item["action"]
            params = action_item.get("parameters", {})
            
            param_str = ", ".join(f"{k}='{v}'" if isinstance(v, str) else f"{k}={v}" for k, v in params.items())
            print(f"Step {i+1}: {action}({param_str})")