# NAO Robot Planner with qiBullet & OpenAI

A PyBullet-based simulator for NAO robot with AI-driven action planning.

## Features

- **OpenAI-Powered Action Planning**: Generates robot action sequences from natural language instructions
- **Full NAO Robot Simulation**: Control speech, movement, and gestures in a PyBullet environment
- **Multiple Action Types**: Movement, gestures, speech, and vision capabilities

## Environment setup

- Virtual conda environment with Python 3.9 is used since the latest version of qiBullet supports upto Python 3.9.
- For thr chatgpt empowered robot planning paper the openai version used was "openai==0.28.0". This is added in the requirements

## Installation (Ubuntu)

* In your terminal, activate your conda environment with Python 3.9.
```bash
conda activate base
conda activate <your_python_env>
``` 
> The latest supported Python version for qiBullet is 3.9. Newer versions of Python3 will throw error in the code. 
* Clone this repo in your device, and go to the cloned directory.
```bash
cd ~/
git clone https://github.com/alfattah129/nao_planner_qibullet.git
cd ./nao_planner_qibullet
```
* Install the dependencies from the `requirements.txt` file using `pip`.
```bash
python3 -m pip install -r ./requirements.txt
```
> For installing the qiBullet library alone, follow the README section of the qiBullet repository: https://github.com/softbankrobotics-research/qibullet

## Driver issue For conda-based virtual environment users (From Sabik's repo. I didnt face any issues)

I ran into a driver issue while running the simulator. The issue raised because I was using an Anaconda environment. 
According to online information, there is a problem with the libstdc++.so file in Anaconda (I use this commercial python distribution). It cannot be associated with the driver of the system, so we removed it and used the libstdc++ that comes with Linux. so creates a soft link there.

```bash
cd /home/$USER/anaconda3/envs/$ENV/lib
mkdir backup  # Create a new folder to keep the original libstdc++
mv libstd* backup  # Put all libstdc++ files into the folder, including soft links
cp /usr/lib/x86_64-linux-gnu/libstdc++.so.6  ./ # Copy the c++ dynamic link library of the system here
ln -s libstdc++.so.6 libstdc++.so
ln -s libstdc++.so.6 libstdc++.so.6.0.19
```
Here, `$ENV` is the name of the conda environment.

I found the solution in here:
https://stackoverflow.com/questions/72110384/libgl-error-mesa-loader-failed-to-open-iris

## About this repo


### `nao_agent.py`
Contains the class for controlling the Nao robot in simulation. The methods in this class represent all available actions for the robot. Feel free to modify or extend these methods.

**Available Actions:**
- `speak(speech=text)`: Make the robot say the specified text
- `stand()`: Set the joint angles for a standing posture
- `sit()`: Set the joint angles for a sitting posture *(UNDER DEVELOPMENT)*
- `wave(hand=right/left)`: Wave the specified hand twice (default: `right`)
- `nod_head(direction=up_down/right_left)`: Nod head in "yes" or "no" gesture (default: `up_down`)
- `turn_head(direction=right/left)`: Turn head left or right (default: `right`)
- `gaze_head(direction=up/down)`: Gaze up or down (default: `up`)
- `raise_arms(hand=left/right/both)`: Raise specified arm(s) (default: `both`)
- `walk(x=x,y=y)`: Walk to specified coordinates *(UNDER DEVELOPMENT)*
- `handshake(hand=right/left)`: Perform handshake (default: `right`)
- `reset_nao_pose()`: Reset to default standing pose
- `capture_image(camera=top/bottom)`: Capture image from camera (default: `top`)
- `stream_video(camera=top/bottom/both)`: Start video stream (default: `top`). Press Space to stop.

### `robot_planner.py`
Contains the AI-powered action planner that uses OpenAI's API to convert natural language instructions into executable action sequences for the NAO robot.

**Key Features:**
- Uses GPT-3.5-turbo model for action planning
- Converts natural language to structured JSON action plans
- Validates actions against available NAO capabilities
- Handles parameter generation for complex actions

**Example Workflow:**
1. User inputs: "Wave with your left hand, then say hello"
2. Planner generates:
```json
{
  "actions": [
    {
      "action": "wave",
      "parameters": {"hand": "left"}
    },
    {
      "action": "speak",
      "parameters": {"speech": "hello"}
    }
  ]
}

### `main.py`: `main.py` serves as the central controller that connects the NAO robot simulation with AI-powered planning. It takes natural language instructions from users, generates corresponding action plans via `robot_planner.py`, and executes them step-by-step on the virtual NAO robot through `nao_agent.py`, while handling errors and maintaining proper timing between actions. The script runs in a continuous loop until the user enters "stop", providing an interactive way to test all of the robot's capabilities.

    > **Note:** Make sure the qiBullet installation is done successfully before trying out the `main.py` or any of your own code. Keep the `nao_agent.py` and 'robot_planner.py' file in the same directory as the code you're trying to run, so that the Nao class can be accessed.

## Useful References

* Example code files are available here: https://github.com/softbankrobotics-research/qibullet/tree/master/examples
* Posture control examples: https://github.com/softbankrobotics-research/qibullet/wiki/Tutorials:-Virtual-Robot
* qiBullet Nao robot class and available methods: https://github.com/softbankrobotics-research/qibullet/blob/master/qibullet/nao_virtual.py# planner_qibullet
