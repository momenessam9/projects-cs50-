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
    
    int key = atoi(argv[1]) % 26;
    string text = get_string("plaintext:  ");
    bool cap;
    int chr;
    for (int i = 0; i < strlen(text); i++)
    {
        chr = text[i];
        cap = false;
        printf("0yaay %c %i\n",  text[i], text[i]);
        if (isupper(text[i]))
        {
            cap = true;
            text[i] = tolower(text[i]);
            printf("1yaay %c %i\n",  text[i], text[i]);
        }
        if (islower(text[i]))
        {
            int rem;
            chr = text[i] + key;
            printf("2yaay %c %i\n",  chr, chr);
                  
            if (chr > 122)
            {
                rem = chr - 122;
                text[i] = 96 + rem;
                printf("3yaay %c %i\n",  text[i], text[i]);
            }
            else
            {
                text[i] = chr;
            }
            if (cap)
            {
                text[i] = toupper(text[i]);
                printf("4yaay %c %i\n",  text[i], text[i]);
            }
        }
           
    }
    printf("ciphertext: %s\n", text);
}

