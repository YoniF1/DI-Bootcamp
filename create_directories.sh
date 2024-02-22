#!/bin/bash

mkdir -p Week1/Day{1..5}/{ExercisesXP,ExercisesXPGold,ExercisesXPNinja,DailyChallenge}
cd Week1

for day in Day{1..5}/; do
    for dir in ExercisesXP ExercisesXPGold ExercisesXPNinja DailyChallenge; do
        touch "$day$dir"/{index.html,style.css}
    done
done
