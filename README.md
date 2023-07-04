# Never-Remember
Version 1.0

Never Remember is a Python app that utilizes JSON to help you remember important dates through notifications when you turn on your computer.

The app consists of two main components:

1. Python: Python is a versatile programming language that enables you to develop applications with ease. In this case, Python is used for various tasks such as sending notifications and handling JSON data.

2. JSON: JSON (JavaScript Object Notation) is a lightweight data interchange format commonly used for storing and transmitting data. JSON is employed here to store the important dates and associated information.

The basic functionality of the Never Remember app can be summarized as follows:

1. Create a JSON file: Set up a JSON file to store the important dates and their relevant data. Each entry in the file can include details like the event name, date, and any additional information you wish to remember.

2. Write a Python script: Develop a Python script that runs in the background when your computer starts up. This script reads the JSON file and compares the current date with the dates stored in the file.

3. Check for upcoming events: Iterate through the dates in the JSON file and compare them with the current date. Identify any upcoming events that match the current date or fall within a specified range.

4. Display notifications: Utilize a Python library or framework to display notifications on your computer's desktop. Depending on your operating system, you can use libraries such as `win10toast` for Windows or `pync` for macOS.

5. Schedule the script: Configure the script to run automatically when you turn on your computer, ensuring it remains active and able to send notifications when necessary.

In summary, Never Remember is a Python app that utilizes JSON to help you remember important dates by sending notifications when you start your computer. It is a convenient way to ensure you don't forget significant events and stay informed about your commitments.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

MIT License

Copyright (c) 2021 Martín José Imoberdorf

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
