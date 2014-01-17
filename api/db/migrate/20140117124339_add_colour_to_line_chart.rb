class AddColourToLineChart < ActiveRecord::Migration
  def change
    add_column :line_charts, :colour, :string
  end
end
