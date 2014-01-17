class LineChartsController < ApplicationController
	def edit
	    @line_chart = LineChart.find(params[:id])
	end

	def show
		@line_chart = LineChart.find(params[:id])

	    respond_to do |format|
	      format.html # show.html.erb
	      format.json { render json: @line_chart.to_json(:include => :series) }
	    end
	end

	def new
		@line_chart = LineChart.new
		3.times do
			@line_chart.series.build
		end

		logger.info @line_chart.series

		respond_to do |format|
	      format.html # new.html.erb
	      format.json { render json: @line_chart }
	    end
	end

	def index
		@line_charts = LineChart.all

	    respond_to do |format|
	      format.html # index.html.erb
	      format.json { render json: @line_charts.to_json(:include => :rows) }
	    end
	end

	def update
	    @line_chart = LineChart.find(params[:id])

	    respond_to do |format|
	      if @line_chart.update_attributes(params[:line_chart])
	        format.html { redirect_to :back, notice: 'line_chart was successfully updated.' }
	        format.json { head :no_content }
	      else
	        format.html { render action: "edit" }
	        format.json { render json: @line_chart.errors, status: :unprocessable_entity }
	      end
	    end
	  end

	def create
    @line_chart = LineChart.new(params[:line_chart])

    respond_to do |format|
      if @line_chart.save
        format.html { redirect_to @line_chart, notice: 'line_chart was successfully created.' }
        format.json { render json: @line_chart, status: :created, location: @line_chart }
      else
        format.html { render action: "new" }
        format.json { render json: @line_chart.errors, status: :unprocessable_entity }
      end
    end
  end
end