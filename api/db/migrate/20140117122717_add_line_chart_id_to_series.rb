class AddLineChartIdToSeries < ActiveRecord::Migration
  def change
    add_column :series, :line_chart_id, :integer
  end
end
