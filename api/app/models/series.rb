class Series < ActiveRecord::Base
  attr_accessible :label, :values, :colour
  belongs_to :line_chart
end
