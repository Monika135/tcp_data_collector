import logging
from ..db_session import ScopedSession
from models.device_model import DeviceCards

def device_record_list(device_id, records):
    local_session = ScopedSession()
    try:
        device_records = (
            local_session.query(DeviceCards
                                ).filter_by(device_id=device_id
                                            ).order_by(DeviceCards.created_at.desc()
                                                       ).limit(records).all()
                                                       )
        data = [{
            'id': r.id,
            'device_id': r.device_id,
            'card_id': r.card_id,
            'timestamp': r.timestamp.isoformat() if r.timestamp else None,
            'created_at': r.created_at.isoformat() if r.created_at else None
        } for r in device_records]

        local_session.close()
        return True, data

    except Exception as e:
        logging.error("device_records_list error", exc_info=e)
        return False, "Unable to fetch device records"