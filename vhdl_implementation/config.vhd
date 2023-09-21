library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

package CONFIG is
	type INPUT is array (natural range <>) of integer range 0 to 255;
	signal connection : INPUT (11 downto 0);
	--connection 2 downto 0 is the input of the neural network
	--connection 11 downto 10 is the output of the neural network

	-- int Arrays with Constants
	type constIntArray is ARRAY (natural range <>) of integer;
	constant networkStructure : constIntArray (2 downto 0) := (2,7,3);
	constant connnectionRange : constIntArray (3 downto 0) := (12,10,3,0);
	constant weights : constIntArray (43 downto 0) := (-2323,-148,31,-75,101,-126,34,-80,3508,84,-98,68,-112,94,-92,45,-6377,340,13,-176,14324,-223,84,197,-3886,160,-51,-165,2445,-277,95,260,-3630,267,-45,-196,13643,-217,87,189,2524,154,-26,-123);

	--mapping the 2D network to the 1D Array with the weights
	type KOORDINATES is array (0 to 7, 1 to 2) of natural;
	constant positions: KOORDINATES:=( 
				(0,28),
				(4,36),
				(8,44),
				(12,0),
				(16,0),
				(20,0),
				(24,0),
				(28,0));

	-- Ranges for the sum inside a neuron and the multiplication of an input signal with a weight
	constant maxSumRange: integer:=131071;
	constant minSumRange: integer:=-131072;
	constant maxMultRange: integer:=131071;
	constant minMultRange: integer:=-131072;

	-- -- Array for all multiplication results inside a neuron
	type multResults is ARRAY (natural range <>) of integer range minMultRange to maxMultRange;
end CONFIG;
