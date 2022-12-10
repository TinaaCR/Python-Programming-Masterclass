flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily"
]

# for flower in flowers:
#     print(flower)

separator = " | "
output = separator.join(flowers)    # obs! join funksjonen fungerer bare for strings, ikke et tall feks
print(output)

print(", ".join(flowers))
