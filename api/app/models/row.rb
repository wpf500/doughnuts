class Row < ActiveRecord::Base
  belongs_to :infographic
  attr_accessible :colour, :label, :value

  def to_json
  	{
  		label: self.label,
  		value: self.value,
  		colour: self.colour
  	}
  end
end
