#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>


int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caeser key\n");
        return 1;
    } 
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (isdigit(argv[1][i]))
        {
        }
        else
        {
            printf("Usage: ./caeser key\n");
            return 1;  
        }
    }
    
    int key = atoi(argv[1]);
    string text = get_string("plaintext: ");
    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            int chr = text[i];
            if (isupper(text[i]))
            {
                char cas = tolower(chr);
                text[i] = cas + key;
                if (text[i] <= 0 || text[i] == 127 || ispunct(text[i]))
                {
                    cas = chr - key;
                    text[i] = toupper(cas);
                }
                else
                {                  
                    text[i] = toupper(cas);
                }
            }
            else
            {
                text[i] = chr + key;
            }
            if (text[i] <= 0 || text[i] == 127 || ispunct(text[i]))
            {
                text[i] = chr - key;
            }
        }
    }
    printf("ciphertext: %s\n", text); 
}

