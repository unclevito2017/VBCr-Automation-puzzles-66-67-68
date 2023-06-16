import subprocess
import time
import os
import signal

def run_vbcr(start_keyspace, end_keyspace):
    output_filename = f'{start_keyspace[:3]}.txt'  # Generate the output filename based on the start keyspace
    command = f'VBCr.exe -t 3 -gpu -gpuId 0 -begr {start_keyspace} -endr {end_keyspace} -r 5000 -o {output_filename} -drk 1 -dis 1 -c 13zb1hQ'

    process = subprocess.Popen(command, shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
    time.sleep(500)  # Wait for 600 seconds
    os.kill(process.pid, signal.CTRL_BREAK_EVENT)  # Send CTRL_BREAK_EVENT signal to terminate the process group
    process.wait()  # Wait for the process to exit

# Main loop
start_keyspace = '20000000000000000'  # Starting keyspace value
end_keyspace = '20100000000000000'  # Ending keyspace value
increment = '100000000000000'  # Increment value

while int(end_keyspace, 16) <= int('3ffffffffffffffff', 16):  # Continue until the ending keyspace value is reached
    run_vbcr(start_keyspace, end_keyspace)
    start_keyspace = hex(int(end_keyspace, 16) + 1)[2:]  # Increment the start keyspace value
    end_keyspace = hex(int(start_keyspace, 16) + int(increment, 16) - 1)[2:]  # Increment the end keyspace value correctly
    time.sleep(5)  # Wait for 5 seconds before restarting
