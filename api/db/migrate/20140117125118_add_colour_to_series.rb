class AddColourToSeries < ActiveRecord::Migration
  def change
    add_column :series, :colour, :string
  end
end
