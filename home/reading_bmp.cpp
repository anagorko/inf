#include<fstream>
#include<iostream>
#include <bitset>

using namespace std;

const char file_name[] = "VENUS.BMP";
char* memblock;

void loadImage()
{
	streampos size;

	ifstream file(file_name, ios::in | ios::binary | ios::ate);
	if (file.is_open())
	{
		size = file.tellg();
		memblock = new char[size];
		file.seekg(0, ios::beg);
		file.read(memblock, size);
		file.close();
		//cout << "the entire file content is in memory" << endl;

		//delete[] memblock;
	}
	else cout << "Unable to open file" << endl;
}


void readImage()
{
	size_t iterator = 0;
	//File type
	string filetype;
	filetype.resize(2);
	memcpy(&filetype[0], &memblock[iterator], 2);
	iterator += 2;
	cout <<"filetype: " <<filetype << endl;
	uint32_t size;
	memcpy(&size, &memblock[iterator], sizeof(size));
	iterator += sizeof(size);
	cout <<"size in memory: " <<size << endl;
	iterator += 2;
	iterator += 2;
	uint32_t offset;
	memcpy(&offset, &memblock[iterator], sizeof(offset));
	iterator += sizeof(offset);
	cout << "offset: " << bitset<32>(offset) << endl;
	uint32_t size_of_a_heather;
	memcpy(&size_of_a_heather, &memblock[iterator], sizeof(size_of_a_heather));
	iterator += sizeof(size_of_a_heather);
	cout << "size of heather: " << (size_of_a_heather) << endl;
}
int main()
{
	loadImage();
	readImage();

	return 0;
}
