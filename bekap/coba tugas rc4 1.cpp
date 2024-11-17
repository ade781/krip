#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>

using namespace std;

void xorEn(const string &input, char key)
{
    string output = input;

    // Loop untuk setiap karakter dalam input
    for (size_t i = 0; i < input.size(); i++)
    {
        // Lakukan operasi XOR antara karakter input dan kunci
        output[i] = input[i] ^ key;
    }
    cout << output << endl;
}

void KSA(int S[], const string &key)
{
    int j = 0;
    int keyLength = key.length();

    for (int i = 0; i < 256; i++)
    {
        S[i] = i;
    }

    for (int i = 0; i < 256; i++)
    {
        j = (j + S[i] + key[i % keyLength]) % 256;
        swap(S[i], S[j]);
    }
}

void PRGA(int S[], string &output, const string &input)
{
    int i = 0, j = 0;

    for (size_t n = 0; n < input.length(); n++)
    {
        i = (i + 1) % 256;
        j = (j + S[i]) % 256;
        swap(S[i], S[j]);
        int keystream = S[(S[i] + S[j]) % 256];
        output[n] = input[n] ^ keystream;
    }
}

string RC4(const string &input, const string &key)
{
    int S[256];
    KSA(S, key);

    string output = input;
    PRGA(S, output, input);

    return output;
}

string toHex(const string &input)
{
    stringstream ss;
    for (unsigned char c : input)
    {
        ss << hex << setw(2) << setfill('0') << (int)c;
    }
    return ss.str();
}

string fromHex(const string &input)
{
    string output;
    for (size_t i = 0; i < input.length(); i += 2)
    {
        string byteString = input.substr(i, 2);
        char byteValue = (char)strtol(byteString.c_str(), nullptr, 16);
        output += byteValue;
    }
    return output;
}
