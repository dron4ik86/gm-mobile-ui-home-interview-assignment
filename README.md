## Getting Started (MacOS Environment)

These instructions will guide you on how to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- [Python](https://www.python.org/downloads/)

### Installation

Follow these steps to setup your development environment:

1. Navigate to the repository where you want to save the project.
    ```
    cd <folder name>
    ```
2. Clone the repository.
    ```
    git clone https://github.com/dron4ik86/gm-mobile-ui-home-interview-assignment.git
    ```
3. Install the virtual environment.
    ```
    pip3 install virtualenv
    ```
4. Create a virtual environment in the project directory.
    ```
    cd gm-mobile-ui-home-interview-assignment
    virtualenv venv
    ```
5. Activate the virtual environment.
    ```
    source venv/bin/activate
    ```
6. Install project dependencies.
    ```
    pip3 install -r requirements.txt
    ```
7. Install node.
   ```
   brew install node
   ```
8. Check node and npm version (verify that node was installed).
   ```
   node -v 
   npm -v
   ```
9. Install Appium.
   ```
   npm i -g appium@next
   ```
10. Install latest uiautomator2 driver (for Android platform)
   ```
   appium driver install uiautomator2
   ```
11. Install appium-doctor. Use appium-doctor to easily check and set up the necessary drivers and settings for Appium, streamlining your test environment preparation.
   ```
   npm install @appium/doctor -g
   ```
12. Install Java.
   ```
   brew install openjdk@11
   java -version
   ```
13. Install [Android Studio](https://developer.android.com/studio)
14. Using nano to Edit .zshrc File
   ```
   nano ~/.zshrc
   ```
15. Setting JAVA_HOME and ANDROID_HOME: 
   ```
   export JAVA_HOME=/Library/Java/JavaVirtualMachines/openjdk.jdk/Contents/Home/
   export ANDROID_HOME=/Users/<username>/Library/Android/sdk
   export PATH=$ANDROID_HOME/platform-tools:$PATH
   export PATH=$ANDROID_HOME/platform-tools/bin:$PATH
   export PATH=$ANDROID_HOME/tools:$PATH
   export PATH=$ANDROID_HOME/tools/bin:$PATH
   ```
16. Download the [Appium Inspector](https://github.com/appium/appium-inspector/releases) it displays the properties of UI elements, 
such as their IDs, classes, and other attributes, which are crucial for writing automated tests.
17. Before running the automation test on an Android device, you need to turn on the developer mode on your device. Please follow these steps:
   ```
   1. Go to your device's settings.
   2. Scroll down and tap on 'About phone'.
   3. Tap on 'Software information'.
   4. Tap several times on 'Build number' until you see the message 'Developer mode has been enabled'.
   5. Go back to your device's settings.
   6. Scroll down and tap on 'Developer options'.
   7. Scroll down and enable 'USB debugging'.
   8. Connect your device to your computer. 
   9. You will get the message 'Allow USB debugging?' Press the 'Allow' button.
   10. You will get the message 'Allow access to phone data?' Press the 'Allow' button.
   ```
18. Open the terminal and run the Appium server.
   ```
   appium
   ```
19. Open 'Appium Inspector' and update the 'Capability Builder'. You also can update the 'JSON Representation'. See example:
   ```
   {
  "platformName": "android",
  "appium:deviceName": "RFCWB18Z1JR",
  "appium:automationName": "uiautomator2",
  "appium:noReset": "true",
  "appium:app": "/Absolute/Path/To/<app name>.apk"
   }
   ```
   To get the `deviceName` you can open the terminal and enter this command `adb devices`
   and in the 'List of devices attached' you will see the device name.
20. Please update the `.env.template` file with your own secret values and rename it to `.env`.

### Usage
1. Run tests via behave
   ```
    behave -D platform=android -D device_id=R5CT71Y78DJ -D app_path=/path/to/app.apk " "-D execution_mode=local"
   ```
 



## Troubleshooting

### **Problem 1**:
While checking the output of `appium-doctor` command - The following error was seen

```
apkanalyzer could NOT be found in /Users/<username>/Library/Android/sdk!
```

**Solution**:

The solution was to enable Android SDK Command-line tools from Android Studio Preferences:
1. Open the Android Studio Settings.
2. In search field search for 'Android SDK'.
3. Go to 'SDK Tools' tab.
4. Install the 'Android SDK Command-line Tools'


### **Problem 2**:
### Issue: `zsh: command not found: virtualenv`

If you encounter the following error when trying to activate the virtual environment on macOS:
```
zsh: command not found: virtualenv
```
**Solution**:

This error occurs because the `virtualenv` command is not found in your shell's PATH. Instead, you can use Python's built-in `venv` module to create and activate a virtual environment:
```
python3 -m venv venv
```

