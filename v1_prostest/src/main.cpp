#include "main.h"
#include <iostream>
#include <string>
#include <sstream>

#define DIGITAL_SENSOR_PORT 'D' //uses PORT D to connect GND and Data pin to Nano's GPIO
#define MOTOR_PORT 1 // left motor connected to Smart Port 1 of VexV5 Brain

void opcontrol() {
	pros::lcd::initialize();
	pros::ADIDigitalIn button1 (DIGITAL_SENSOR_PORT);
	pros::Motor leftm (MOTOR_PORT);
	 std::string foo = "UNINIT";
	 std::stringstream bar(foo);
	 pros::lcd::set_text(2,foo);

	 //----------------------------
	 // For moving the left motor based on Nano's digital signal
	 //----------------------------
   while (true) {
		 if(button1.get_value()){
			 leftm = 30;
			 pros::delay(50);
		 }
		 leftm = 0;
	 }

		 /*
		 //--------------------------
		 // For printing text from PROS Terminal to VexV5 Screen
		 //--------------------------
		 //std::cin >> foo;
		 foo = "";
		 getline(std::cin, foo);
		 //std::cin.ignore(2,'\n');
		 if (!foo.empty()) {
						 pros::lcd::set_text(2,foo);
		 }
		 std::cout << std::endl << "donkey\n" << std::endl;
		 std::cout << std::endl << foo << std::endl;

		 pros::delay(2000);
   }
	 */
}
