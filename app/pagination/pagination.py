class Pagination:
    def paginate_query(self, query, page, per_page):
        page = max(1, page)

        paginated_query = query.paginate(page=page, per_page=per_page, error_out=False)

        paginated_items = paginated_query.items

        next_page = paginated_query.next_num if paginated_query.has_next else None
        prev_page = paginated_query.prev_num if paginated_query.has_prev else None

        result = {
            'items': paginated_items,
            'page': paginated_query.page,
            'total_pages': paginated_query.pages,
            'total_items': paginated_query.total,
            'next_page': next_page,
            'prev_page': prev_page,
        }

        return result
