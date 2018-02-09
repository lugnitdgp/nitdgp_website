require 'sinatra'

get '/department/:dep' do
  @department = params[:dep]
  erb :department
  # "This is #{params[:dep]} department"
end

get '/department' do
  erb :department_list
end


get '/' do
  erb :index
end
