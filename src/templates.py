template = """Använd följande kontext för att svara på frågan i slutet. 
Om du inte vet svaret, försök inte hitta på ett svar. 
Skriv om frågan så att den innehåller relevant information
Säkerställ att svaret innehåller all information som krävs för att besvara frågan.. 
    Kontext:
    ```    
    {context}
    ```

    Fråga:
    ``` 
    {question}
    ```

    Hjälpfullt svar:"""
