def calculateFine(frequency, duration, ayys)
    fine = (((duration.to_f * 2) + (ayys.to_f * 5))/100.0)  * frequency.to_f
    return fine.round(2)
end
