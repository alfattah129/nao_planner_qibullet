## qiBullet simulator

A PyBullet based simulator for NAO and Pepper robot.

## Environment setup

- I've used a virtual conda environment with Python 3.9 since the latest version of qiBullet supports upto Python 3.9. 

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

## Driver issue (For conda-based virtual environment users)

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

- `nao_agent.py`: Contains the class for the Nao robot for the simulation. The methods in this class are the actions available for the robot. Feel free to check these methods out or modify them. Available actions are: 
    * `speak(speech=text)`: Speak out the input text.
    * `stand()`: Set the joint angles for a standing posture.
    * `sit()`: Set the joint angles for a sitting posture. *(UNDER DEVELOPMENT)*
    * `wave(hand=right/left)`: Wave a preferrend hand twice. Default is `right`.
    * `nod_head(direction=up_down/right_left)`: Nod head in a "yes" or "no" gesture. Default is `up_down`.
    * `turn_head(direction=right/left)`: Turn head left or right. Default is `right`.
    * `gaze_head(direction=up/down)`: Turn head up or down. Default is `up`.
    * `raise_arms(hand=left/right/both)`: Raise a preferred arm or both arms. Default is `both`.
    * `walk(x=x,y=y)`: Walk to a specified coordinate. *(UNDER DEVELOPMENT)*
    * `handshake(left/right)`: Do a handshake motion with a preferred hand. Default is `right`.
    * `reset_nao_pose()`: Reset the Nao robot to the standing pose.
    * `capture_image(top/bottom)`: Returns an image captured from the `top` or `bottom` camera of the Nao robot. Default is `top`.
    * `stream_video(top/bottom/both)`: Start a realtime video stream from a specified or both cameras using `opencv`. Default is `top`. Hit Space to terminate the stream.

- `main.py`: The main file for the simulation. You can try out different features/actions of the robot in it. Here's an example snippet to get started:

    ```python
    from nao_agent import Nao
    import time

    simulation = Nao(gui=True) # robot instance

    # try out actions
    nao.speak("I am Nao, I am a robot.")
    time.sleep(5.0) # wait for 5s
    ```
    > **Note:** Make sure the qiBullet installation is done successfully before trying out the `main.py` or any of your own code. Keep the `nao_agent.py` file in the same directory as the code you're trying to run, so that the Nao class can be accessed.

## Useful References

* Example code files are available here: https://github.com/softbankrobotics-research/qibullet/tree/master/examples
* Posture control examples: https://github.com/softbankrobotics-research/qibullet/wiki/Tutorials:-Virtual-Robot
* qiBullet Nao robot class and available methods: https://github.com/softbankrobotics-research/qibullet/blob/master/qibullet/nao_virtual.py# planner_qibullet
