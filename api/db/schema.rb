# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended to check this file into your version control system.

ActiveRecord::Schema.define(:version => 20140117135400) do

  create_table "infographics", :force => true do |t|
    t.string   "title"
    t.string   "source"
    t.string   "chart_type"
    t.datetime "created_at",  :null => false
    t.datetime "updated_at",  :null => false
    t.string   "subtitle"
    t.string   "inner_label"
  end

  create_table "line_charts", :force => true do |t|
    t.string   "title"
    t.string   "yLabel"
    t.string   "xLabels"
    t.datetime "created_at", :null => false
    t.datetime "updated_at", :null => false
    t.string   "colour"
    t.string   "chart_type"
  end

  create_table "rows", :force => true do |t|
    t.integer  "value"
    t.string   "label"
    t.string   "colour"
    t.datetime "created_at",     :null => false
    t.datetime "updated_at",     :null => false
    t.integer  "infographic_id"
  end

  create_table "series", :force => true do |t|
    t.string   "label"
    t.string   "values"
    t.datetime "created_at",    :null => false
    t.datetime "updated_at",    :null => false
    t.integer  "line_chart_id"
    t.string   "colour"
  end

end
