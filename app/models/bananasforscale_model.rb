def howMany(value)
    
    # units = {
    # :banana => {:inches => 7.0, :grams => 140.4, :ml => 140.0},
    # :corgi => {:inches => 24.0, :grams => 11339.8, :ml => "?"},
    # :joebiden => {:inches => 72.0, :grams => 92000.0, :ml => "?"}
    # }
    
    if @newunit == "bananas"
        if @unittype == "inches"
        @divideby = 7.0
        puts "banana-inches"
        elsif @unittype == "grams"
        @divideby = 140.4
        puts "banana-grams (lol)"
        elsif @unittype == "pounds"
        @divideby = 0.3095
        puts "banana-pounds"
        elsif @unittype == "feet"
        @divideby = 0.584
        puts "banana-feet"
        elsif @unittype == "miles"
        @divideby = 0.00011048
        puts "banana-miles"
        end
        
        
    elsif @newunit == "corgis"
        if @unittype == "inches"
        @divideby = 24.0
        puts "corgi-inches"
        elsif @unittype == "grams"
        @divideby = 11339.8
        puts "corgi-grams"
        elsif @unittype == "pounds"
        @divideby = 25.0
        puts "corgi-pounds"
        elsif @unittype == "feet"
        @divideby = 2.0
        puts "corgi-feet"
        elsif @unittype == "miles"
        @divideby = 0.000378788
        puts "corgi-miles"
        end
        
    elsif @newunit == "joebidens"
        if @unittype == "inches"
        @divideby = 72.0
        puts "biden-inches"
        elsif @unittype == "grams"
        @divideby = 92000.0
        puts "biden-grams"
        elsif @unittype == "pounds"
        @divideby = 202.8
        puts "biden-pounds"
        elsif @unittype == "feet"
        @divideby = 6.0
        puts "biden-feet"
        elsif @unittype == "miles"
        @divideby = 0.00113636
        puts "biden-miles"
        end
        
    end #big if (beginning at line 9)
    
    
    total = value.to_f/@divideby.to_f
    return total
    
end #method howMany (beginning at line 1)
