class AddInnerLabelToInfographic < ActiveRecord::Migration
  def change
    add_column :infographics, :inner_label, :string
  end
end
