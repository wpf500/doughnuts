class LineChart < ActiveRecord::Base
	has_many :series
  attr_accessible :title, :xLabels, :yLabel, :series, :series_attributes, :chart_type
  accepts_nested_attributes_for :series, :reject_if => lambda { |a| a[:values].blank? }, :allow_destroy => true

  def embed_url
    "http://localhost:5000/render/line/#{self.id}"
  end

  def to_json args
  	json = JSON.parse super
  	clean = {}

  	clean['title'] = json['title']
  	clean['type'] = json['chart_type']
  	clean['source'] = 'doughnuts'

  	clean['x_labels'] = json['xLabels'].split(',')

  	clean['rows'] = json['series'].map do |s|
  		{
  			label: s['label'],
  			colour: s['colour'],
  			value: s['values'].split(',').map(&:to_i)
  		}
  	end

  	# clean['rows'] = []

  	# json['series'].each {|r|
  	# 	clean['series'] << {
  	# 		label: r['label'],
  	# 		value: r['value'],
  	# 		colour: r['colour']
  	# 	}
  	# }

  	clean
  end
end
