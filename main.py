import sys
from nao_agent import Nao
from robot_planner import RobotPlanner  # Import the RobotPlanner class
import time

def execute_plan(nao, plan):
    """
    Execute the generated plan using the Nao robot.
    """
    if not plan or "actions" not in plan:
        print("Invalid plan received")
        return
    
    print("\n=== Executing Action Plan ===")
    for i, action_item in enumerate(plan["actions"]):
        action = action_item["action"]
        params = action_item.get("parameters", {})
        
        print(f"Step {i+1}: Executing {action} with parameters {params}")
        
        # Map the action to the corresponding Nao method
        if action == "speak":
            nao.speak(**params)
        elif action == "stand":
            nao.stand()
        elif action == "sit":
            nao.sit()
        elif action == "wave":
            nao.wave(**params)
        elif action == "nod_head":
            nao.nod_head(**params)
        elif action == "turn_head":
            nao.turn_head(**params)
        elif action == "gaze_head":
            nao.gaze_head(**params)
        elif action == "raise_arms":
            nao.raise_arms(**params)
        elif action == "move":
            # Ensure all required parameters are present
            if "x" not in params or "y" not in params or "theta" not in params:
                print(f"Error: Missing parameters for 'move'. Required: x, y, theta.")
                continue
            nao.move(**params)
        elif action == "handshake":
            nao.handshake(**params)
        elif action == "reset_nao_pose":
            nao.reset_nao_pose()
        else:
            print(f"Unknown action: {action}")
        
        time.sleep(1.0)  # Add a delay between actions for better visualization

if __name__ == "__main__":
    # Initialize the Nao robot
    nao = Nao(gui=True)
    time.sleep(1.0)  # Allow time for the robot to initialize

    # Initialize the RobotPlanner
    planner = RobotPlanner()

    # Continuous input loop
    while True:
        # Prompt the user for an instruction
        instruction = input("\nEnter an instruction for Nao (or type 'stop' to end): ")
        
        # Stop execution if the user types "stop"
        if instruction.lower() == "stop":
            print("Stopping the Nao robot.")
            break
        
        # Generate the action plan
        print(f"Generating plan for instruction: {instruction}")
        plan = planner.generate_plan(instruction)

        # Execute the plan
        if plan:
            execute_plan(nao, plan)
        else:
            print("Failed to generate a plan")

    # Stop the nao
    nao.shutdown()