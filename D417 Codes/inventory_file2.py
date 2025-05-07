inventory = ( 
"""WindowsDesktop-1: 
    General_Settings: 
      Name: WindowsDesktop-1
      RAM: 4096 MB
      vCPUs: 2
      QEMU_binary: /bin/qemu-system-x86_64(v4.2.1)
      Boot_Priority: HDD
      On_close: Send the shutdown signal (ACPI)
      Console_type: vnc
    Network_Settings: 
      Adapters: 1
      Base_MAC: 0c:4b:3c:0a:00:00
      Type: Intel Gigabit Ethernet (e1000)
      Replicate_network_connection_states_in_QEMU: True

  WindowsDesktop-2: 
    General_Settings: 
      Name: WindowsDesktop-2
      RAM: 4096 MB
      vCPUs: 2
      QEMU_binary: /bin/qemu-system-x86_64(v4.2.1)
      Boot_Priority: HDD
      On_close: Send the shutdown signal (ACPI)
      Console_type: vnc
    Network_Settings: 
      Adapters: 1
      Base_MAC: 0c:59:fd:86:00:00
      Type: Intel Gigabit Ethernet (e1000)
      Replicate_network_connection_states_in_QEMU: True

  WindowsDesktop-3: 
    General_Settings: 
      Name: WindowsDesktop-3
      RAM: 4096 MB
      vCPUs: 2
      QEMU_binary: /bin/qemu-system-x86_64(v4.2.1)
      Boot_Priority: HDD
      On_close: Send the shutdown signal (ACPI)
      Console_type: vnc
    Network_Settings: 
      Adapters: 1
      Base_MAC: 0c:e2:07:f3:00:00
      Type: Intel Gigabit Ethernet (e1000)
      Replicate_network_connection_states_in_QEMU: True

  WindowsDesktop-4: 
    General_Settings: 
      Name: WindowsDesktop-4
      RAM: 4096 MB
      vCPUs: 2
      QEMU_binary: /bin/qemu-system-x86_64(v4.2.1)
      Boot_Priority: HDD
      On_close: Send the shutdown signal (ACPI)
      Console_type: vnc
    Network_Settings: 
      Adapters: 1
      Base_MAC: 0c:46:74:35:00:00
      Type: Intel Gigabit Ethernet (e1000)
      Replicate_network_connection_states_in_QEMU: True

  Test_Box_1: 
    General_Settings: 
      Name: Test_Box_1
      RAM: 4096 MB
      vCPUs: 2
      QEMU_binary: /bin/qemu-system-x86_64(v4.2.1)
      Boot_Priority: HDD
      On_close: Send the shutdown signal (ACPI)
      Console_type: vnc
    Network_Settings: 
      Adapters: 1
      Base_MAC: 0c:cb:a8:90:00:00
      Type: Intel Gigabit Ethernet (e1000)
      Replicate_network_connection_states_in_QEMU: True """)

print(inventory) 
