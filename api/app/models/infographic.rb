class Infographic < ActiveRecord::Base
  has_many :rows
  accepts_nested_attributes_for :rows, :reject_if => lambda { |a| a[:value].blank? }, :allow_destroy => true
  attr_accessible :chart_type, :source, :subtitle, :title, :rows, :rows_attributes, :inner_label

  def embed_url
    "/chart/render/doughnut/#{self.id}"
  end

  def to_json args
  	json = JSON.parse super
  	clean = {}

  	clean['title'] = json['title']
  	clean['subtitle'] = json['subtitle']
  	clean['source'] = json['source']
  	clean['type'] = json['chart_type']
    clean['inner_label'] = json['inner_label']
  	clean['rows'] = []

  	json['rows'].each {|r|
  		clean['rows'] << {
  			label: r['label'],
  			value: r['value'],
  			colour: r['colour']
  		}
  	}

  	clean
  end
end
