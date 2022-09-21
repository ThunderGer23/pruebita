def bddEntity(items) -> dict:
    return {
        "File":{
            "_id": items.id,
            "route": items.route,
            "text_of_file": items.text_of_file,
            "text_analized": items.text_analized,
            "update_at": items.update_at,
            "date": items.date
        }
    }