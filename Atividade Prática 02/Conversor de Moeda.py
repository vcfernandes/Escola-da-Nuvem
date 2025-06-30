valor_reais = 100.00 
taxa_dolar = 5.20    
taxa_euro = 6.15      

valor_dolar = valor_reais / taxa_dolar

valor_euro = valor_reais / taxa_euro

print(f"Com R$ {valor_reais:.2f}, você pode comprar:")
print(f"US$ {valor_dolar:.2f} (Dólares)") 
print(f"€ {valor_euro:.2f} (Euros)")     