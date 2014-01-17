class CreateLineCharts < ActiveRecord::Migration
  def change
    create_table :line_charts do |t|
      t.string :title
      t.string :yLabel
      t.string :xLabels

      t.timestamps
    end
  end
end
