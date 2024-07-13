# Note this only applies to Amazon urls

url = ("https://www.amazon.com/playStation%C2%AE5-console-slim-playStation-5/dp/B0CL61F39H/ref=sr_1_1?crid"
       "=2KHK99ASBMVDE&dib=eyJ2IjoiMSJ9.AHjTd7ZFe8s8RHzX7QExwDesCneAdSrHHQ5Jj2D66rukbEu4CS"
       "-dNurH8EkX9Fqgf6RZ7ZBhOIQYoCPJQ1CJpeuMAceOiHDsex4Pr_kI-Epl4qIEf37BPzJ4UcpazIz0tRrfF_NnIUy2_PuFqt59qqiAW"
       "-kPVE9D_PEasGCOLG_mbqtXK_oU_Rm4lt7nlHEqCVbxPBJO1cbQvoCmJqJDSikAlOUJ_rzPYbpuoQSooZk"
       ".2jSCLblCVM3S0KUOfpD4K6P_3nalMsRVmc589EJSfgM&dib_tag=se&keywords=playstation%2B5&qid=1718985490&sprefix=play"
       "%2Caps%2C232&sr=8-1&th=1")


start_index = url.index(".com/") + 5

print(start_index)

end_index = url.index("/dp")

print(end_index)

product_name = url[start_index:end_index]

print(product_name.title().replace("-", " "))
