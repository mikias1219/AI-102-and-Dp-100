#!/usr/bin/env python3
"""
Monitor Azure ML Compute Instance Status
"""

import time
import subprocess
import json

def get_compute_status():
    """Get the current status of the compute instance"""
    try:
        result = subprocess.run([
            "az", "ml", "compute", "show",
            "--name", "ml-compute-instance"
        ], capture_output=True, text=True, timeout=30)

        if result.returncode == 0:
            data = json.loads(result.stdout)
            state = data.get('provisioning_state', 'Unknown')
            compute_state = data.get('state', 'Unknown')
            return state, compute_state
        else:
            return "Error", result.stderr.strip()
    except Exception as e:
        return "Error", str(e)

def main():
    print("🔍 Monitoring Azure ML Compute Instance: ml-compute-instance")
    print("=" * 60)

    while True:
        provisioning_state, compute_state = get_compute_status()

        if provisioning_state == "Error":
            print(f"❌ Error: {compute_state}")
            break

        print(f"📊 Provisioning State: {provisioning_state}")
        print(f"🔄 Compute State: {compute_state}")

        if provisioning_state == "Succeeded" and compute_state == "Running":
            print("✅ Compute instance is ready!")
            print("\n🎉 You can now:")
            print("   • Use this compute instance for training jobs")
            print("   • Run notebooks in Azure ML Studio")
            print("   • Submit experiments to this compute target")
            break
        elif provisioning_state == "Succeeded" and compute_state == "Stopped":
            print("🛑 Compute instance is stopped. Start it in Azure ML Studio.")
            break
        elif provisioning_state == "Failed":
            print("❌ Compute instance creation failed.")
            break

        print("⏳ Still provisioning... (checking again in 30 seconds)")
        print("-" * 60)
        time.sleep(30)

if __name__ == "__main__":
    main()