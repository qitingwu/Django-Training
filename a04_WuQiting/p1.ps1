# name: Qiting Wu   netId: qitwu    Student ID: 112064080

# Problem 1 (15 points): p1.ps1
# Sometimes the processes running on your computer escape from your benevolent control and so must be
# killed. Let's write a powershell script to do this work for us.
# Task:
# Your script should do the following:
# 1. Read a process name as a command-line argument
# 2. List all currently running instances of that process on the console.
# 2a. If there is no currently running instance of the specified process, then print out the message,
#  "No such process is running." to the console, and then terminate the script.
# 3. Kill all currently running instances of the specified process.
# 4. List all currently running processes on the console, so we can see the specified process is absent.
# Parsing the arguments:
# The script takes a single command-line argument. The argument is a string that names a process.
# Script name:
# Name your shell script: p1.ps1
# Example invocation: $ powershell p1.ps1

param( [string] $proc_name = $(throw "Please specify a process name."))

$p = Get-Process -Name $proc_name 2>$null

if ($p) {
    $p | Out-Host
    $p | Stop-Process
    Get-Process
}else {
    "No such process is running."
}

