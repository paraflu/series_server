
@("https://it.wikipedia.org/wiki/9-1-1:_Lone_Star",
    "https://it.wikipedia.org/wiki/The_Good_Doctor_(serie_televisiva)",
    "https://it.wikipedia.org/wiki/9-1-1_(serie_televisiva)",
    "https://it.wikipedia.org/wiki/Station_19",
    "https://it.wikipedia.org/wiki/The_Resident_(serie_televisiva)",
    "https://it.wikipedia.org/wiki/Transplant"
) | ForEach-Object {
    write-host $_
    invoke-restmethod -method POST http://localhost:5000/api/parse -body @{"url" = $_ }
}
