class Row < ActiveRecord::Base
  belongs_to :infographic
  attr_accessible :colour, :label, :value
end
