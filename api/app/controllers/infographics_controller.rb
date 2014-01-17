class InfographicsController < ApplicationController
  # GET /infographics
  # GET /infographics.json
  def index
    @infographics = Infographic.all

    respond_to do |format|
      format.html # index.html.erb
      format.json { render json: @infographics.to_json(:include => :rows) }
    end
  end

  # GET /infographics/1
  # GET /infographics/1.json
  def show
    @infographic = Infographic.find(params[:id])

    respond_to do |format|
      format.html # show.html.erb
      format.json { render json: @infographic.to_json(:include => :rows) }
    end
  end

  # GET /infographics/new
  # GET /infographics/new.json
  def new
    @infographic = Infographic.new
    # @infographic.rows.build
    3.times { @infographic.rows.build }

    respond_to do |format|
      format.html # new.html.erb
      format.json { render json: @infographic }
    end
  end

  # GET /infographics/1/edit
  def edit
    @infographic = Infographic.find(params[:id])
  end

  # POST /infographics
  # POST /infographics.json
  def create
    @infographic = Infographic.new(params[:infographic])

    respond_to do |format|
      if @infographic.save
        format.html { redirect_to @infographic, notice: 'Infographic was successfully created.' }
        format.json { render json: @infographic, status: :created, location: @infographic }
      else
        format.html { render action: "new" }
        format.json { render json: @infographic.errors, status: :unprocessable_entity }
      end
    end
  end

  # PUT /infographics/1
  # PUT /infographics/1.json
  def update
    @infographic = Infographic.find(params[:id])

    respond_to do |format|
      if @infographic.update_attributes(params[:infographic])
        format.html { redirect_to :back, notice: 'Infographic was successfully updated.' }
        format.json { head :no_content }
      else
        format.html { render action: "edit" }
        format.json { render json: @infographic.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /infographics/1
  # DELETE /infographics/1.json
  def destroy
    @infographic = Infographic.find(params[:id])
    @infographic.destroy

    respond_to do |format|
      format.html { redirect_to infographics_url }
      format.json { head :no_content }
    end
  end
end
