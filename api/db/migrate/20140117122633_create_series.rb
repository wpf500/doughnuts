class CreateSeries < ActiveRecord::Migration
  def change
    create_table :series do |t|
      t.string :label
      t.string :values

      t.timestamps
    end
  end
end
