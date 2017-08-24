require './config/environment'
require './app/models/bananasforscale_model'
require './app/models/meganproofer_model'
require './app/models/dabjarcalculator_model'


class ApplicationController < Sinatra::Base
  configure do
    set :public_folder, 'public'
    set :views, 'app/views'
  end

  get '/' do
    erb :index
  end
  
  get '/construction.erb' do
    erb :construction
  end
  
  get '/bananasforscale.erb' do
    erb :bananasforscale
  end
  
  get '/meganproofer.erb' do
    erb :meganproofer
  end
  
  get '/dabjarcalculator.erb' do
    erb :dabjarcalculator
  end
  
  get '/cdd.erb' do
    erb :cdd
  end
 
  post '/uselesscalculating' do
    @unitval = params["unitVal"]
    @unittype = params["unitType"]
    @newunit = params["newUnit"]
    @uselessanswer = howMany(@unitval)
    erb :uselessanswer
  end
  
  post '/meganproofd' do
    @string = params["string"]
    @proofdanswer = meganProof(@string)
    erb :meganproofd
  end
  
  post '/totalfine' do
  @dabfrequency = params["dabfrequency"]
  @dabduration = params["dabduration"]
  @ayys = params["ayys"]
  @fine = calculateFine(@dabfrequency, @dabduration, @ayys)
  erb :totalfine
  end

end
